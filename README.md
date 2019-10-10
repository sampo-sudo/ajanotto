# Ajanotto kahdella Raspberry Pi:llä langattomasti

Ensin luotiin serveri. Luotiin ensin Apache serveri, mutta Flask serveri oli se johon päädyttiin, koska se näytti toimivan tässä paremmin. (Tarvittiin terminaalista oikeat sovellukset ja kirjastot.) Ip-osoitteet piti selvittää jonka jälkeen sisäisessä verkossa laitteet pingasivat jo toisiaan. Eli ihan yksinkertainen python serveri flaskilla ilman mitään socketteja tai muuta.

Tarvittiin siis serveri ja clientti, joka lähettää joko post tai get requesteja serverille eli toiselle Raspille.
Koodin ei sisälly sensoreita eli oikeaa välimatkaa se ei mittaa. (Ideana oli siis mitata 60m juoksun aika langattomasti...)
Koodissa ei myöskään ole käytetty mitää threadingia ja ajanoton nopeutta eikä signaalin siirtymisen virhemarginaaleja ole otettu huomioon.


