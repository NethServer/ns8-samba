# import-users input Schema

```txt
http://schema.nethserver.org/ns8-samba/api-moduled/handlers/import-users/validate-input.json
```

Import users and groups definitions in AD, with optional attribute merge behavior.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                     |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :----------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [validate-input.json](import-users/validate-input.json "open original schema") |

## import-users input Type

`object` ([import-users input](validate-input-1.md))

## import-users input Examples

```json
[
  {
    "skip_existing": true,
    "records": [
      {
        "user": "alice",
        "display_name": "Alice Jordan",
        "password": "secret",
        "locked": false,
        "groups": [
          "developers"
        ],
        "mail": "alice@nethserver.org",
        "must_change_password": true,
        "no_password_expiration": false
      },
      {
        "user": "bob",
        "display_name": "Robert Smith",
        "password": "secret",
        "locked": false,
        "groups": [
          "support"
        ],
        "mail": "robert@nethserver.org",
        "must_change_password": true,
        "no_password_expiration": false
      }
    ]
  }
]
```

# import-users input Properties

| Property                         | Type      | Required | Nullable       | Defined by                                                                                                                                                                                  |
| :------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [skip\_existing](#skip_existing) | `boolean` | Optional | cannot be null | [import-users input](validate-input-1-properties-skip_existing.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/import-users/validate-input.json#/properties/skip_existing") |
| [records](#records)              | `array`   | Required | cannot be null | [import-users input](validate-input-1-properties-records.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/import-users/validate-input.json#/properties/records")             |

## skip\_existing



`skip_existing`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [import-users input](validate-input-1-properties-skip_existing.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/import-users/validate-input.json#/properties/skip_existing")

### skip\_existing Type

`boolean`

### skip\_existing Default Value

The default value is:

```json
false
```

## records



`records`

* is required

* Type: `object[]` ([Details](validate-input-1-properties-records-items.md))

* cannot be null

* defined in: [import-users input](validate-input-1-properties-records.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/import-users/validate-input.json#/properties/records")

### records Type

`object[]` ([Details](validate-input-1-properties-records-items.md))
