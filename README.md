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
Grundsätzlich kann man rückblickend sagen, dass es öfters Probleme bei den Datentypen in den Klassen gab, welche falsch definiert wurden und im nachhinein neu angepasst werden mussten.


### User Story 1; Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind
Bei den Usterstories 1 waren vor allem die Importe herausfordernd, was nach einigen Recherchen reibungslos funktionierte. Ebenfalls eine grosse Herausforderung war die Trennung der Business Logic und dem Data Access, also welche Informationen wo hinterlegt werden. 

### User Story 2; Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.


### User Story 3; Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.


### User Story 4; Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.


### User Story 5; Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.


### User Story 6; Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice.


### User Story 7; Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.


### User Story 8; Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten. 


### User Story 9; Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.


### User Story 10; Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.


### User Story DB-Schemaänderung 1; Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer).


### User Story Datenvisulaisieurng ??;



# Vorgehen in der Gruppe
In diesem Modul stellte sich die Aufteilung der Arbeiten sehr schwer, vor allem aus dem Grund, dass kein Mitglied Erfahrungen mit Python hatte. Es war für uns ziemlich herausfordernd, das Gelernte im Unterricht am geeigneten Ort im Projekt umzusetzen.
Nach anfänglichem Ausprobieren teilten wir die Aufgaben in die drei Teile, model, data_access und business_logic auf, jede Person übernahm einen davon.
Nachdem die Models befriedigend umgesetzt wurden, stellte sich schnell heraus, dass diese Aufgabenteilung für die individuelle Weiterentwicklung und die Fertigstellung des Projektes wenig sinnvoll war.
Aufgrund des immer näher rückenden Abgabetermins und des Zeitmangels wegen den Erwärbstätigkeiten mancher Gruppenmitglieder wurde das Projekt die verschiedenen Userstories aufgeteilt und bearbeitet.
Dies klappte nach anfänglichen Unsicherheiten bei der Umsetzung erstaunlich gut. 

