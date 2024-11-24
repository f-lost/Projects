# Analisi e Visualizzazione delle Correlazioni

Questa funzione esegue un'analisi approfondita delle correlazioni tra variabili numeriche in un DataFrame, filtrandole in base alle sue colonne categoriali. Le funzioni principali calcolano le correlazioni, generano heatmap e pairplot, e salvano i risultati in un file JSON per un'analisi successiva.

## Caratteristiche

- **Calcolo delle Correlazioni**: Calcola le correlazioni tra le colonne numeriche del DataFrame.
- **Salvataggio delle Heatmap**: Salva heatmap visive delle correlazioni tra variabili numeriche.
- **Generazione dei Pairplot**: Se richiesto, genera pairplot per le colonne con correlazioni significative.
- **Salvataggio dei Risultati**: Salva le correlazioni significative in un file JSON.
- **Gestione Automatica delle Cartelle**: Crea una cartella per salvare i file generati e gestisce automaticamente i conflitti di nome delle cartelle.

## Prerequisiti

Sono necessari i seguenti pacchetti:

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`