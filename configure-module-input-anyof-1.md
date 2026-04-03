# Untitled undefined type in configure-module input Schema

```txt
http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/1
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [configure-module-input.json\*](samba/configure-module-input.json "open original schema") |

## 1 Type

unknown

# 1 Properties

| Property                | Type          | Required | Nullable       | Defined by                                                                                                                                                                      |
| :---------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [realm](#realm)         | Not specified | Optional | cannot be null | [configure-module input](configure-module-input-anyof-1-properties-realm.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/1/properties/realm")         |
| [provision](#provision) | Not specified | Optional | cannot be null | [configure-module input](configure-module-input-anyof-1-properties-provision.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/1/properties/provision") |

## realm

AD Domain/Realm and NS8 User Domain name

`realm`

* is optional

* Type: unknown

* cannot be null

* defined in: [configure-module input](configure-module-input-anyof-1-properties-realm.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/1/properties/realm")

### realm Type

unknown

### realm Constraints

**maximum length**: the maximum number of characters for this string is: `140`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$
```

[try pattern](https://regexr.com/?expression=%5E%5Ba-zA-Z0-9%5D%5B-a-zA-Z0-9%5D%7B0%2C62%7D\(%5C.%5Ba-zA-Z0-9%5D%5B-a-zA-Z0-9%5D%7B0%2C62%7D\)%2B%24 "try regular expression with regexr.com")

## provision



`provision`

* is optional

* Type: unknown

* cannot be null

* defined in: [configure-module input](configure-module-input-anyof-1-properties-provision.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/1/properties/provision")

### provision Type

unknown

### provision Constraints

**constant**: the value of this property must be equal to:

```json
"join-domain"
```
