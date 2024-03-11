import uuid

class Texte:
    def __init__(self, titre, auteur, source, date_publication,
                contenu, categorie, etiquettes):
        self.id_text = uuid.uuid4()
        self.titre = titre
        self.auteur = auteur
        self.source = source
        self.date_publication = date_publication
        self.contenu = contenu
        self.categorie = categorie
        self.etiquettes = etiquettes
