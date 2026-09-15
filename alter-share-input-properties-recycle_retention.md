# Untitled integer in alter-share input Schema

```txt
http://schema.nethserver.org/samba/alter-share-input.json#/properties/recycle_retention
```

Number of days deleted files are retained in the Recycle Bin before permanent removal. 0 = Infinite

| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :---------------------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [alter-share-input.json\*](samba/alter-share-input.json "open original schema") |

## recycle\_retention Type

`integer`

## recycle\_retention Constraints

**minimum**: the value of this number must greater than or equal to: `0`
