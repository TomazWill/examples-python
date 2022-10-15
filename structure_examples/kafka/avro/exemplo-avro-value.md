
### Objeto
```json
[
    {
        "page_title": "Antoine Meillet", 
        "page_id": 3, 
        "contributors": [
            {
                "revisions": 2, "username": "Curry"
            },
            {
                "revisions": 1, "username": " script de conversão"
            },
            {
                "revisions": 1, "username": "Francis"
            }
        ]
    }
]
```

### Objeto Avro
```json
{
    "namespace": "org.wikipedia.fr",
    "name": "meta-history",
    "type": "record",
    "fields": [
        {
            "name": "page_title",
            "type": "string"
        },
        {
            "name": "page_id",
            "type": "int"
        },
        {
            "name": "contributors",
            "type": {
                "type": "array",
                "items": {
                    "type": "record",
                    "name": "contribution",
                    "fields": [
                        {
                            "name": "revisions",
                            "type": "int"
                        },
                        {
                            "name": "username",
                            "type": "string"
                        }
                    ]
                }
            }
        }
    ]
}
```