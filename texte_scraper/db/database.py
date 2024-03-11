import csv
import re
import mysql.connector
import uuid


class CreoleTextDatabase:
    def __init__(self, host, user, password, db_name):
        self.conn = self.connect(host, user, password, db_name)
        self.cursor = self.conn.cursor()

    def connect(self, host, user, password, db_name):
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        print(conn)
        return conn

    def close_connection(self):
        self.conn.close()
        self.cursor.close()

    def insert_into_textes(self, text_obj):
        sql = "INSERT INTO textes (id_text, titre, auteur, source, date_publication, contenu, categorie, etiquettes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        self.cursor.execute(sql, (str(text_obj.id_text), text_obj.titre, text_obj.auteur, text_obj.source,
                            text_obj.date_publication, text_obj.contenu, text_obj.categorie, text_obj.etiquettes))

        self.conn.commit()

    def get_all_texts(self):
            sql = "SELECT id_text, titre, auteur, source, date_publication, contenu, categorie, etiquettes, version FROM textes"
            self.cursor.execute(sql)
            results = self.cursor.fetchall()

            textes = []
            for result in results:
                text_obj = (
                    result[0],
                    result[1],
                    result[2],
                    result[3],
                    result[4],
                    result[5],
                    result[6],
                    result[7],
                    result[8]
                )
                textes.append(text_obj)

            return textes
    
    def process_and_insert_text(self, text_obj, id_text):
        # Remove special characters
        processed_text = re.sub(r'[^a-zA-Z0-9\sàèòÀÈÒ]', ' ', text_obj.contenu)

        # Remove duplicate texts
        if self.is_duplicate_text(id_text, processed_text):
            return

        # Normalize text case
        processed_text = processed_text.lower()

        # Remove unnecessary spaces
        # processed_text = ' '.join(set(processed_text.split()))

        # Remove HTML tags
        processed_text = re.sub(r'<.*?>', '', processed_text)

        # Insert processed text into the database with version=1
        self.insert_processed_text(text_obj.titre, text_obj.auteur, text_obj.source, text_obj.date_publication, 
                                processed_text, text_obj.categorie, text_obj.etiquettes, version=1)

    def is_duplicate_text(self, id_text, processed_text):
        # Check if the processed text already exists for the given id_text
        sql = "SELECT id_text FROM textes WHERE id_text = %s AND contenu = %s"
        self.cursor.execute(sql, (str(id_text), processed_text))
        return bool(self.cursor.fetchone())

    def insert_processed_text(self, titre, auteur, source, date_publication, processed_text, categorie, etiquettes, version):
        sql = "INSERT INTO textes (id_text, titre, auteur, source, date_publication, contenu, categorie, etiquettes, version) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (str(uuid.uuid4()), titre, auteur, source,
                            date_publication, processed_text, categorie, etiquettes, version))
        self.conn.commit()

    def get_id_text_and_contenu(self):
        sql = "SELECT id_text, contenu FROM textes WHERE version = 1"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()

        id_text_and_contenu = []
        for result in results:
            id_text_and_contenu.append((result[0], result[1]))

        return id_text_and_contenu

    def write_to_csv(self, file_path):
        id_text_and_contenu = self.get_id_text_and_contenu()

        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['id_text', 'contenu'])  # Write header

            for row in id_text_and_contenu:
                csv_writer.writerow(row)