# alter-share input Schema

```txt
http://schema.nethserver.org/samba/alter-share-input.json
```

Alter a shared folder

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :---------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [alter-share-input.json](samba/alter-share-input.json "open original schema") |

## alter-share input Type

`object` ([alter-share input](alter-share-input.md))

## alter-share input Examples

```json
{
  "name": "myshare002",
  "browseable": true,
  "description": "With Samba Audit",
  "enable_audit": true,
  "log_failed_events": false
}
```

```json
{
  "name": "myshare002",
  "browseable": true,
  "description": "Second share",
  "enable_recycle": true,
  "recycle_retention": 30
}
```

```json
{
  "name": "myshare001",
  "browseable": false,
  "description": "New description"
}
```

# alter-share input Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                       |
| :---------------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [browseable](#browseable)                 | `boolean` | Optional | cannot be null | [alter-share input](alter-share-input-properties-browseable.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/browseable")               |
| [enable\_recycle](#enable_recycle)        | `boolean` | Optional | cannot be null | [alter-share input](alter-share-input-properties-enable_recycle.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/enable_recycle")       |
| [recycle\_retention](#recycle_retention)  | `integer` | Optional | cannot be null | [alter-share input](alter-share-input-properties-recycle_retention.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/recycle_retention") |
| [enable\_audit](#enable_audit)            | `boolean` | Optional | cannot be null | [alter-share input](alter-share-input-properties-enable_audit.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/enable_audit")           |
| [log\_failed\_events](#log_failed_events) | `boolean` | Optional | cannot be null | [alter-share input](alter-share-input-properties-log_failed_events.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/log_failed_events") |
| [name](#name)                             | `string`  | Required | cannot be null | [alter-share input](alter-share-input-properties-name.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/name")                           |
| [description](#description)               | `string`  | Optional | cannot be null | [alter-share input](alter-share-input-properties-description.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/description")             |

## browseable

If true the share is browseable to users, and is listed as a server resource. If false users must know its name to connect with it because it is not included in the network share list.

`browseable`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [alter-share input](alter-share-input-properties-browseable.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/browseable")

### browseable Type

`boolean`

### browseable Default Value

The default value is:

```json
true
```

## enable\_recycle

Enable the Recycle Bin for this network share.

`enable_recycle`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [alter-share input](alter-share-input-properties-enable_recycle.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/enable_recycle")

### enable\_recycle Type

`boolean`

## recycle\_retention

Number of days deleted files are retained in the Recycle Bin before permanent removal. 0 = Infinite

`recycle_retention`

* is optional

* Type: `integer`

* cannot be null

* defined in: [alter-share input](alter-share-input-properties-recycle_retention.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/recycle_retention")

### recycle\_retention Type

`integer`

### recycle\_retention Constraints

**minimum**: the value of this number must greater than or equal to: `0`

## enable\_audit

Enable the basic audit log for the share

`enable_audit`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [alter-share input](alter-share-input-properties-enable_audit.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/enable_audit")

### enable\_audit Type

`boolean`

## log\_failed\_events

Add failed events to the audit log

`log_failed_events`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [alter-share input](alter-share-input-properties-log_failed_events.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/log_failed_events")

### log\_failed\_events Type

`boolean`

## name

The name of the share and of the underlying directory

`name`

* is required

* Type: `string`

* cannot be null

* defined in: [alter-share input](alter-share-input-properties-name.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/name")

### name Type

`string`

### name Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## description

Free text for share comment or description

`description`

* is optional

* Type: `string`

* cannot be null

* defined in: [alter-share input](alter-share-input-properties-description.md "http://schema.nethserver.org/samba/alter-share-input.json#/properties/description")

### description Type

`string`
