# Untitled string in add-share input Schema

```txt
http://schema.nethserver.org/samba/add-share-input.json#/properties/name
```

The name of the share and of the underlying directory. Ref <https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file#naming-conventions>

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [add-share-input.json\*](samba/add-share-input.json "open original schema") |

## name Type

`string`

## name Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")
