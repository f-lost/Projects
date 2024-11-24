# Analisi e Visualizzazione delle Correlazioni

Questa libreria Python esegue un'analisi approfondita delle correlazioni tra variabili numeriche in un DataFrame, concentrandosi su colonne categoriali. Le funzioni principali calcolano le correlazioni, generano heatmap e pairplot, e salvano i risultati in un file JSON per un'analisi successiva.

## Caratteristiche

- **Calcolo delle Correlazioni**: Calcola le correlazioni tra le colonne numeriche del DataFrame, escludendo la diagonale (correlazione di una variabile con sé stessa).
- **Salvataggio delle Heatmap**: Salva heatmap visive delle correlazioni tra variabili numeriche.
- **Generazione dei Pairplot**: Se richiesto, genera pairplot per le colonne con correlazioni significative.
- **Salvataggio dei Risultati**: Salva le correlazioni significative in un file JSON.
- **Gestione Automatica delle Cartelle**: Crea una cartella per salvare i file generati e gestisce automaticamente i conflitti di nome delle cartelle.

## Prerequisiti

Assicurati di avere Python 3.x installato sul tuo sistema. Puoi scaricare Python da [python.org](https://www.python.org/downloads/).

Installa i seguenti pacchetti Python necessari:

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`

Puoi installare questi pacchetti utilizzando `pip`:

```bash
pip install pandas numpy seaborn matplotlib
