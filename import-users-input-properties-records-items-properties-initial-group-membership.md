# Initial group membership Schema

```txt
http://schema.nethserver.org/samba/import-users-input.json#/properties/records/items/properties/groups
```

Set the user as a member of the given list of groups

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [import-users-input.json\*](samba/import-users-input.json "open original schema") |

## groups Type

`string[]`

## groups Constraints

**unique items**: all items in this array must be unique. Duplicates are not allowed.
