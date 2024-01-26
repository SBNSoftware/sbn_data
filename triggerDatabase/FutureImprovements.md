Comment from Joseph Zennamo (Fermilab), 
info from Justin Mueller 

The read back from this database is a little 
slow due to the fact that this database is 
not indexed. If we want to index this database
we can run this command:

```
sqlite3 <db>
sqlite> CREATE INDEX i1 ON triggerdata(run_number);
```

the reason this wasn't done already is that it 
increases the database file size above the 
github file size limit (from ~85 MB to ~125 MB). 

