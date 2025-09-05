# Untitled integer in add-share input Schema

```txt
http://schema.nethserver.org/samba/add-share-input.json#/properties/recycle_retention
```

Number of days deleted files are retained in the Recycle Bin before permanent removal. 0 = Infinite

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [add-share-input.json\*](samba/add-share-input.json "open original schema") |

## recycle\_retention Type

`integer`

## recycle\_retention Constraints

**minimum**: the value of this number must greater than or equal to: `0`
