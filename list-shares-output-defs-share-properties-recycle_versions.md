# Untitled boolean in list-shares output Schema

```txt
http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_versions
```

Keeps multiple versions of deleted files with the same name. If false, only the latest version is retained.

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-shares-output.json\*](samba/list-shares-output.json "open original schema") |

## recycle\_versions Type

`boolean`

## recycle\_versions Default Value

The default value is:

```json
false
```
