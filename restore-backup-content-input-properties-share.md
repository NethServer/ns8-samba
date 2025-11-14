# Untitled string in restore-backup-content input Schema

```txt
http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/share
```

Seek the paths of this Samba share

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [restore-backup-content-input.json\*](mail/restore-backup-content-input.json "open original schema") |

## share Type

`string`

## share Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")
