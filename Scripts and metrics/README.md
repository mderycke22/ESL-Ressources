# Scripts

## Contenu

- `app_queries.json`: les requêtes du projet exportées par SQLInspect
- `export_queries.py`: script Python permettant d'extraire les requêtes commençant par `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE` ou `CREATE INDEX` (utilisé pour l'extraction du schéma physique explicite). Exemple d'utilisation: `$ python export_queries.py app_queries.json schema.sql`
- `create_database.sql`: le code DDL extrait grâce au script `export_queries.py` et réarrangé
- `analyserAppQueries.py`: Ce script nous a principalment été utile pour compter le nombre de requêtes (générées par SQLInspect) par type (SELECT, INSERT, UPDATE, DELETE)
- `createGraph.py`: Ce script nous a permis de générer des graphiques, principalement pour comparer les requetes par tables présente dans le fichier `queries_stats.json`(requetes générées par SQLInspect + des requetes supplémentaires ajoutées manuellement par nous)
