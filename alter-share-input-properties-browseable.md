# Untitled boolean in alter-share input Schema

```txt
http://schema.nethserver.org/samba/alter-share-input.json#/properties/browseable
```

If true the share is browseable to users, and is listed as a server resource. If false users must know its name to connect with it because it is not included in the network share list.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [alter-share-input.json\*](samba/alter-share-input.json "open original schema") |

## browseable Type

`boolean`

## browseable Default Value

The default value is:

```json
true
```
