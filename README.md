# AEP_Hotelreservierungssystem

### Rollen

Entwickler - Yannick Krähenbühl, Cesco Meggiolaro, Tobias Mutz, Jennifer Studer

Coaches -  Sandro Schwander, Phillip Gachnang

# Klassendiagramm

![2.Sem AEP.jpg](images/2.Sem%20AEP.jpg)

Das Klassendiagramm dient als Grundlage für die Objektstruktur, Geschäftslogik und Datenpersistenz in Python.
### Guest
Repräsentiert einen registrierten Gast, der eine Buchungen buchen, stornieren und den Buchungsverlauf anzeigen kann.

### Booking
Verbindet die Gästen mit Zimmern zu den bestimmten Zeiträumen, z.B. mit den Attributen check_in_date, check_out_date, is_cancelled, total_amount.
Mögliche Methoden sind die Buchungsdaten zu ändern oder den Zahlungsbetrag zu berechnen.

### Room
Beinhaltet Informationen zu Zimmern in Hotels, welche Listen von RoomType und Facility enthält, die mit der Logik zur Zimmerauswahl verwendet wird. 

### Hotel
Repräsentiert ein Hotel mit Name, Adresse, Sterne und der Zimmerliste.

### Invoice
Wird bei einer Buchung erstellt, berechnet und speichert den Betrag und generiert ein pdf Dokument der Rechnung, welche direkt zum Gast gesendet wird.

### Admin
Der Admin hat Rechte zur Verwaltung der Benutzer, Hotels, Buchungen etc.

### Address
Enthält die Adressen von Guest, Hotel und Admin.

### Facility
Zusatzleistungen im Hotel, z.B. Spa, WLAN, ein Zimmer kann mehrere Facility-Objekte beinhalten.

### RoomType
Definiert die Art des Zimmers (Einelzimmer, Suite, Doppelzimmer) und die maximale Anzahl der Gäste pro Zimmer.

## Beziehungen
Guest -> Booking: 1:n

Booking -> Room: 1:1

Hotel -> Room: 1:n

Room -> Facility: m:n

Booking -> Invoice: 1:1

Admin, Guest -> Address: 1:1

# Projektstruktur, Überblick
Die [model](model) definieren die Datenstrukturen, die im gesamten Projekt verwendet werden. 
Die Datenbankoperation kapselt der [data_access](data_access). Darin wird die Verfügbarkeit der Abfragen gewährleistet, welche in der [business_logic](business_logic) definiert werden.

# Umsetzung User Stories
Sämtliche UserStory Abfragen werden in einem seperaten Jupyter Notebook ([user_stories.ipynb](user_stories.ipynb)) abgefragt. 

# Vorgehen in der Gruppe
In diesem Modul stellte sich die Aufteilung der Arbeiten sehr schwer, vor allem aus dem Grund, dass kein Mitglied Erfahrungen mit Python hatte. Es war für uns ziemlich herausfordernd, das Gelernte im Unterricht am geeigneten Ort im Projekt umzusetzen.
Nach anfänglichem Ausprobieren teilten wir die Aufgaben in die drei Teile, model, data_access und business_logic auf, jede Person übernahm einen davon.
Nachdem die Models befriedigend umgesetzt wurden, stellte sich schnell heraus, dass diese Aufgabenteilung für die individuelle Weiterentwicklung und die Fertigstellung des Projektes wenig sinnvoll war.
Aufgrund des immer näher rückenden Abgabetermins und des Zeitmangels wegen den Erwärbstätigkeiten mancher Gruppenmitglieder wurde das Projekt die verschiedenen Userstories aufgeteilt und bearbeitet.
Dies klappte nach anfänglichen Unsicherheiten bei der Umsetzung erstaunlich gut. 



