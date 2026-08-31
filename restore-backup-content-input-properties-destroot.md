# Untitled string in restore-backup-content input Schema

```txt
http://schema.nethserver.org/mail/restore-backup-content-input.json#/properties/destroot
```

Name of a share root-level directory where content is restored. Existing content is removed before restoring the backup.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [restore-backup-content-input.json\*](mail/restore-backup-content-input.json "open original schema") |

## destroot Type

`string`

## destroot Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")
