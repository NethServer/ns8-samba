# Untitled undefined type in configure-module input Schema

```txt
http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/2
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [configure-module-input.json\*](samba/configure-module-input.json "open original schema") |

## 2 Type

unknown

# 2 Properties

| Property                | Type          | Required | Nullable       | Defined by                                                                                                                                                                      |
| :---------------------- | :------------ | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [realm](#realm)         | Not specified | Optional | cannot be null | [configure-module input](configure-module-input-anyof-2-properties-realm.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/2/properties/realm")         |
| [provision](#provision) | Not specified | Optional | cannot be null | [configure-module input](configure-module-input-anyof-2-properties-provision.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/2/properties/provision") |

## realm

A NS8 domain name to obtain the actual AD realm: relax the pattern

`realm`

* is optional

* Type: unknown

* cannot be null

* defined in: [configure-module input](configure-module-input-anyof-2-properties-realm.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/2/properties/realm")

### realm Type

unknown

### realm Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
.+
```

[try pattern](https://regexr.com/?expression=.%2B "try regular expression with regexr.com")

## provision



`provision`

* is optional

* Type: unknown

* cannot be null

* defined in: [configure-module input](configure-module-input-anyof-2-properties-provision.md "http://schema.nethserver.org/samba/configure-module-input.json#/anyOf/2/properties/provision")

### provision Type

unknown

### provision Constraints

**constant**: the value of this property must be equal to:

```json
"join-member"
```
