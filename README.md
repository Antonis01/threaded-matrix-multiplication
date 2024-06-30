# Threaded Matrix Multiplication

## Εκτέλεση Προγράμματος

Για την εκτέλεση του κώδικα πρέπει να γράψουμε στο terminal την εντολή:
```sh
python main.py

-Στη συνέχεια, το πρόγραμμα θα μας ζητήσει να κάνουμε εισαγωγή των διαστάσεων
του πρώτου πίνακα και μετά θα μας εμφανίζει τη θέση του κάθε στοιχείου για το οποίο
εμείς θα δώσουμε έναν αριθμό.

-Όταν τελειώσουμε με την εισαγωγή στοιχείων για τον πρώτο πίνακα, το πρόγραμμα ζητά εισαγωγή
διαστάσεων για τον δεύτερο πίνακα και επαναλαμβάνεται το προηγούμενο βήμα.
Στην περίπτωση όπου οι στήλες του πρώτου πίνακα δεν είναι ίσες με τις γραμμές
του δεύτερου πίνακα, το πρόγραμμα θα τερματιστεί.

-Όταν τελειώσουμε με την εισαγωγή όλων των στοιχείων και στους δύο πίνακες,
θα εμφανιστεί στην οθόνη μας ο χρόνος εκτέλεσης που χρειάστηκε κάθε thread,
το αποτέλεσμα του πολλαπλασιασμού των δύο πινάκων της παράλληλης εκτέλεσης,
και ο συνολικός χρόνος του παράλληλου αλγορίθμου που είναι ίσος με το χρόνο
του thread που χρειάστηκε τον περισσότερο χρόνο να εκτελεστεί.

-Για λόγους σύγκρισης χρόνου, υλοποίησα και τον σειριακό αλγόριθμο πολλαπλασιασμού
δύο πινάκων όπου βλέπουμε ότι έχουμε το ίδιο αποτέλεσμα και ο χρόνος αν έχουμε αρκετά
δεδομένα στους δύο πίνακες, παρατηρούμε ότι χρειάζεται λιγότερο χρόνο στην παράλληλη
εκτέλεση. Αντίθετα, σε περίπτωση που έχουμε πίνακες της τάξης π.χ. 2x2, παρατήρησα
με αρκετές εκτελέσεις ότι η διαφορά των δύο θα είναι πολύ μικρή και μερικές φορές
ο σειριακός μπορεί να εκτελεστεί και γρηγορότερα.
```
Μπορείτε να εκτελέσετε και να δείτε τα αποτελέσματα του κώδικα online από αυτόν τον σύνδεσμο:
https://replit.com/@antonis01/threaded-matrix-multiplication
Demo: https://youtu.be/MVly5NCWlHY?si=SiqTb5bpeKBlfoEK
