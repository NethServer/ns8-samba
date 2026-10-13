# Untitled undefined type in configure-module input Schema

```txt
http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/2/properties/realm
```

A NS8 domain name to obtain the actual AD realm: relax the pattern

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [configure-module-input.json\*](samba/configure-module-input.json "open original schema") |

## realm Type

unknown

## realm Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
.+
```

[try pattern](https://regexr.com/?expression=.%2B "try regular expression with regexr.com")
