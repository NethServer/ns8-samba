# Untitled string in seek-snapshot-contents input Schema

```txt
http://schema.nethserver.org/mail/seek-snapshot-contents-input.json#/properties/share
```

Seek the paths of this Samba share

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                           |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :--------------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [seek-snapshot-contents-input.json\*](mail/seek-snapshot-contents-input.json "open original schema") |

## share Type

`string`

## share Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")
