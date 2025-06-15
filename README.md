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

![Project_Structure.png](images/Project_Structure.png)
In der Datenbank werden sämtliche Daten hinterlegt.
Die [model](model) definieren die Datenstrukturen, die im gesamten Projekt verwendet werden. Ebenfalls werden die model mit Getter und Setter definiert. Der Getter definiert, dass die Daten abgefragt werden können, während der Setter die Eingaben definiert.  
Die Datenbankoperation kapselt der [data_access](data_access). Darin wird die Verfügbarkeit der Abfragen gewährleistet, welche in der [business_logic](business_logic) definiert werden.

# Umsetzung User Stories
Sämtliche UserStory Abfragen werden in einem seperaten Jupyter Notebook ([user_stories.ipynb](user_stories.ipynb)) abgefragt.
Grundsätzlich kann man rückblickend sagen, dass es öfters Probleme bei den Datentypen in den Klassen gab, welche falsch definiert wurden und im nachhinein neu angepasst werden mussten.


### User Story 1; Als Gast möchte ich die verfügbaren Hotels durchsuchen, damit ich dasjenige auswählen kann, welches meinen Wünschen entspricht. Wünsche sind
Bei den Usterstories 1 waren vor allem die Importe herausfordernd, was nach einigen Recherchen reibungslos funktionierte. Ebenfalls eine grosse Herausforderung war die Trennung der Business Logic und dem Data Access, also welche Informationen wo hinterlegt werden. 

### User Story 2; Als Gast möchte ich Details zu verschiedenen Zimmertypen (Single, Double, Suite usw.), die in einem Hotel verfügbar sind, sehen, einschliesslich der maximalen Anzahl von Gästen für dieses Zimmer, Beschreibung, Preis und Ausstattung, um eine fundierte Entscheidung zu treffen.
Die Herausforderung dieser Userstory war die Verknüpfung von room, room_type, booking mit den check_in_date und check_out_date. 

### User Story 3; Als Admin des Buchungssystems möchte ich die Möglichkeit haben, Hotelinformationen zu pflegen, um aktuelle Informationen im System zu haben.
Das Hinzufügen und Löschen von Daten waren nicht eine riesige Herausforderung, lediglich das Update in 3.3 war schwierig umzusetzen. Wir haben einen neuen Wert definiert, das Update durchgeführt und das Ergebnis danach angezeigen lassen.

### User Story 4; Als Gast möchte ich ein Zimmer in einem bestimmten Hotel buchen, um meinen Urlaub zu planen.
Nachdem alle Daten eingegeben wurden, werden alle dafür infragekommenden Räume angezeigt (booking_manager.show_bookings()), danach das gewünschte Zimmer noch einmal geprüft (room_manager.find_available_rooms_by_dates) und zum Schluss die neue Buchung angezeigt (booking_manager.show_bookings()). 

### User Story 5; Als Gast möchte ich nach meinem Aufenthalt eine Rechnung erhalten, damit ich einen Zahlungsnachweis habe. Hint: Fügt einen Eintrag in der «Invoice» Tabelle hinzu.
Es wurde invoice_manager.create_invoice_for_existing_booking(booking_id) eingefügt und alle Attribute ausgedruckt, um die Userstroy auszuführen.

### User Story 6; Als Gast möchte ich meine Buchung stornieren, damit ich nicht belastet werde, wenn ich das Zimmer nicht mehr benötige. Hint: Sorgt für die entsprechende Invoice.
Es ist wichtig, dass die Buchung nicht auf der Datenbank gelöscht wird, sondern lediglich geändert wird mit is_ancelled = True hinterlegt. 

### User Story 7; Als Gast möchte ich eine dynamische Preisgestaltung auf der Grundlage der Nachfrage sehen, damit ich ein Zimmer zum besten Preis buchen kann. Hint: Wendet in der Hochsaison höhere und in der Nebensaison niedrigere Tarife an.


### User Story 8; Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können, um eine Übersicht zu erhalten. 


### User Story 9; Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen, damit ich sie besser bewerben kann.
Mit dem admin_manager.get_logged_in_admin() kann lediglich der Admin über die room_nr die facility_name aufrufen.

### User Story 10; Als Admin möchte ich in der Lage sein, Stammdaten zu verwalten, z.B. Zimmertypen, Einrichtungen, und Preise in Echtzeit zu aktualisieren, damit das Backend-System aktuelle Informationen hat.
Mit dem admin_manager konnte mit dem Update hinterlegt werden, dass man die Daten anpassen kann, ohne die ID zu verändern. Dies wurde für Guest, Address, Invoice, Room, RoomType, Bookng und Hotel übernommen. Nach der Änderung werden die Daten vor und nach dem Update geprintet.

### User Story DB-Schemaänderung 1; Als Admin möchte ich alle Buchungen bearbeiten können, um fehlende Informationen zu ergänzen (z.B. Telefonnummer).
Wir haben uns entschieden, eine neue Tabelle in der Datenbank für den Admin zu erstellen. Dafür wurde eine neue Klasse hinzugefügt (admin_dao.create_admin(admin)) mit den Attributen admin_id, username, password, email, vorname und nachname.

### User Story Datenvisulaisieurng ??;



# Vorgehen in der Gruppe
In diesem Modul stellte sich die Aufteilung der Arbeiten sehr schwer, vor allem aus dem Grund, dass kein Mitglied Erfahrungen mit Python hatte. 
Nach anfänglichem Ausprobieren teilten wir die Aufgaben in die drei Teile, model, data_access und business_logic auf, jede Person übernahm einen davon.
Nachdem die Models befriedigend umgesetzt wurden, stellte sich schnell heraus, dass diese Aufgabenteilung für die individuelle Weiterentwicklung und die Fertigstellung des Projektes wenig sinnvoll war.
Aufgrund des immer näher rückenden Abgabetermins und des Zeitmangels wegen den Erwärbstätigkeiten mancher Gruppenmitglieder wurde das Projekt die verschiedenen Userstories aufgeteilt und bearbeitet.
Dies klappte nach anfänglichen Unsicherheiten bei der Umsetzung erstaunlich gut. 

# Fazit
Das Projekt war deutlich schwieriger und zeitaufwändiger als das vorher besuchte Modul Datenbasierte Unternehmensanwedungen. Vor allem zu Beginn war es schwierig zu verstehen, wo und wie man das Gelernte im Projekt anwenden kann.
Ebenfalls war es organisatorisch spannend das Projekt durchzuführen, da ein Gruppenmitglied die Vorlesungen am Mittwoch besucht hat, während alle anderen Teammitglieder am Montag anwesend waren. Dies benötigte eine gute Organisation und Flexibilität für Besprechungen von allen Parteien.
