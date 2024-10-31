# Scripts

## Contenu

- `app_queries.json`: les requêtes du projet exportées par SQLInspect
- `export_queries.py`: script Python permettant d'extraire les requêtes commençant par `CREATE TABLE`, `DROP TABLE`, `ALTER TABLE` ou `CREATE INDEX` (utilisé pour l'extraction du schéma physique explicite). Exemple d'utilisation: `$ python export_queries.py app_queries.json schema.sql`
- `create_database.sql`: le code DDL extrait grâce au script `export_queries.py` et réarrangé
