# Initial password Schema

```txt
http://schema.nethserver.org/samba/import-users-input.json#/properties/records/items/properties/password
```

If missing, a random password is set

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [import-users-input.json\*](samba/import-users-input.json "open original schema") |

## password Type

`string` ([Initial password](import-users-input-properties-records-items-properties-initial-password.md))

## password Constraints

**maximum length**: the maximum number of characters for this string is: `256`
