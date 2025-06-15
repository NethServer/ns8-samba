# Untitled integer in list-shares output Schema

```txt
http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_retention
```

Number of days deleted files are retained in the Recycle Bin before permanent removal. 0 = Infinite

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                        |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [list-shares-output.json\*](samba/list-shares-output.json "open original schema") |

## recycle\_retention Type

`integer`

## recycle\_retention Constraints

**minimum**: the value of this number must greater than or equal to: `0`
