# add-share input Schema

```txt
http://schema.nethserver.org/samba/add-share-input.json
```

Create a new shared folder

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [add-share-input.json](samba/add-share-input.json "open original schema") |

## add-share input Type

`object` ([add-share input](add-share-input.md))

## add-share input Examples

```json
{
  "name": "myshare002",
  "description": "With Samba Audit",
  "enable_audit": true,
  "browseable": false,
  "log_failed_events": false
}
```

```json
{
  "name": "myshare001",
  "browseable": true,
  "description": "First share"
}
```

```json
{
  "name": "myshare002",
  "description": "Second share",
  "enable_recycle": true,
  "recycle_retention": 30
}
```

```json
{
  "name": "myshare001",
  "description": "First share",
  "group": "g1",
  "permissions": "ergrw"
}
```

# add-share input Properties

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                 |
| :---------------------------------------- | :-------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [browseable](#browseable)                 | `boolean` | Optional | cannot be null | [add-share input](add-share-input-properties-browseable.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/browseable")               |
| [enable\_recycle](#enable_recycle)        | `boolean` | Optional | cannot be null | [add-share input](add-share-input-properties-enable_recycle.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/enable_recycle")       |
| [recycle\_versions](#recycle_versions)    | `boolean` | Optional | cannot be null | [add-share input](add-share-input-properties-recycle_versions.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/recycle_versions")   |
| [recycle\_retention](#recycle_retention)  | `integer` | Optional | cannot be null | [add-share input](add-share-input-properties-recycle_retention.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/recycle_retention") |
| [enable\_audit](#enable_audit)            | `boolean` | Optional | cannot be null | [add-share input](add-share-input-properties-enable_audit.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/enable_audit")           |
| [log\_failed\_events](#log_failed_events) | `boolean` | Optional | cannot be null | [add-share input](add-share-input-properties-log_failed_events.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/log_failed_events") |
| [name](#name)                             | `string`  | Required | cannot be null | [add-share input](add-share-input-properties-name.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/name")                           |
| [description](#description)               | `string`  | Optional | cannot be null | [add-share input](add-share-input-properties-description.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/description")             |
| [group](#group)                           | `string`  | Optional | cannot be null | [add-share input](add-share-input-properties-group.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/group")                         |
| [permissions](#permissions)               | `string`  | Optional | cannot be null | [add-share input](add-share-input-properties-permissions.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/permissions")             |

## browseable

If true the share is browseable to users, and is listed as a server resource. If false users must know its name to connect with it because it is not included in the network share list.

`browseable`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [add-share input](add-share-input-properties-browseable.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/browseable")

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

* defined in: [add-share input](add-share-input-properties-enable_recycle.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/enable_recycle")

### enable\_recycle Type

`boolean`

## recycle\_versions

Keeps multiple versions of deleted files with the same name. If false, only the latest version is retained.

`recycle_versions`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [add-share input](add-share-input-properties-recycle_versions.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/recycle_versions")

### recycle\_versions Type

`boolean`

### recycle\_versions Default Value

The default value is:

```json
false
```

## recycle\_retention

Number of days deleted files are retained in the Recycle Bin before permanent removal. 0 = Infinite

`recycle_retention`

* is optional

* Type: `integer`

* cannot be null

* defined in: [add-share input](add-share-input-properties-recycle_retention.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/recycle_retention")

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

* defined in: [add-share input](add-share-input-properties-enable_audit.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/enable_audit")

### enable\_audit Type

`boolean`

## log\_failed\_events

Add failed events to the audit log

`log_failed_events`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [add-share input](add-share-input-properties-log_failed_events.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/log_failed_events")

### log\_failed\_events Type

`boolean`

## name

The name of the share and of the underlying directory. Ref <https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file#naming-conventions>

`name`

* is required

* Type: `string`

* cannot be null

* defined in: [add-share input](add-share-input-properties-name.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/name")

### name Type

`string`

### name Constraints

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^[^/\\:><"|?*]+$
```

[try pattern](https://regexr.com/?expression=%5E%5B%5E%2F%5C%5C%3A%3E%3C%22%7C%3F*%5D%2B%24 "try regular expression with regexr.com")

## description

Free text for share comment or description

`description`

* is optional

* Type: `string`

* cannot be null

* defined in: [add-share input](add-share-input-properties-description.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/description")

### description Type

`string`

## group

The name of the group with initial permissions

`group`

* is optional

* Type: `string`

* cannot be null

* defined in: [add-share input](add-share-input-properties-group.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/group")

### group Type

`string`

### group Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## permissions

Permissions granted to the given group and to everyone else

`permissions`

* is optional

* Type: `string`

* cannot be null

* defined in: [add-share input](add-share-input-properties-permissions.md "http://schema.nethserver.org/samba/add-share-input.json#/properties/permissions")

### permissions Type

`string`

### permissions Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value     | Explanation |
| :-------- | :---------- |
| `"erw"`   |             |
| `"ergrw"` |             |
| `"grw"`   |             |
