# Initial password Schema

```txt
http://schema.nethserver.org/ns8-samba/api-moduled/handlers/import-users/validate-input.json#/properties/records/items/properties/password
```

If missing, a random password is set

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [validate-input.json\*](import-users/validate-input.json "open original schema") |

## password Type

`string` ([Initial password](validate-input-1-properties-records-items-properties-initial-password.md))

## password Constraints

**maximum length**: the maximum number of characters for this string is: `256`
