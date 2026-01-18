Piattaforma E-commerce con Django

Descrizione del progetto
Il progetto consiste in una simulazione di sito e-commerce realizzata utilizzando il linguaggio Python e il framework Django.

L’applicazione si apre con una homepage contenente la lista dei prodotti disponibili. La navbar include:
- sistema di Login e Registrazione per utenti non autenticati
- sistema di Logout per utenti autenticati
- barra di ricerca dei prodotti
- collegamento alla Home (tramite “Lista Prodotti” o “E-commerce”)

La visualizzazione e l’utilizzo del carrello sono consentiti solo dopo aver effettuato il login. Il numero di elementi presenti nel carrello varia dinamicamente in base agli articoli aggiunti.

---



Funzionalità principali

Homepage e Prodotti
La pagina principale consente di:
- visualizzare nome, immagine e prezzo dei prodotti
- aggiungere prodotti al carrello
- accedere alla pagina di dettaglio del singolo prodotto

Dalla pagina di dettaglio è possibile:
- visualizzare la descrizione completa del prodotto
- aggiungere il prodotto al carrello
- proseguire direttamente al carrello oppure utilizzare l’icona nella navbar
- accedere al carrello

---

Carrello 
All’interno del carrello è possibile:
- visualizzare i prodotti selezionati
- rimuovere i prodotti
- modificare la quantità
- visualizzare il totale dell’ordine
- procedere alla creazione dell’ordine

---

Ordini
Durante la fase di checkout vengono richieste le informazioni di contatto dell’utente:
- nome
- email
- indirizzo
- numero di telefono

L’utente può scegliere se:
- confermare l’ordine
- tornare alla homepage

In caso di conferma, l’ordine viene salvato e l’utente viene reindirizzato alla pagina di conferma ordine.

---

Tecnologie utilizzate
- Python
- Django
- HTML
- Bootstrap (tutti i template utilizzano Bootstrap)

---

Funzionalità implementate

Prodotti (products)
- Modello `Product` con i seguenti campi:
  - nome
  - descrizione
  - prezzo
  - immagine
  - disponibilità
- Pagina con elenco prodotti
- Pagina di dettaglio del singolo prodotto

Carrello (cart)
- Aggiunta prodotti al carrello
- Visualizzazione del carrello
- Modifica quantità prodotti
- Rimozione prodotti
- Calcolo automatico del totale

Ordini (orders)
- Modelli `Order` e `OrderItem`
- Creazione ordine a partire dal carrello
- Salvataggio dati cliente
- Conferma ordine

Utenti (users)
- Registrazione utente
- Login e Logout
- Associazione degli ordini agli utenti autenticati

Backend
Utilizzo del pannello Django Admin per:
- gestione dei prodotti
- visualizzazione degli ordini effettuati
