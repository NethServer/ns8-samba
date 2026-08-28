# list-shares output Schema

```txt
http://schema.nethserver.org/samba/list-shares-output.json
```

Return the list of shared folders and their attributes

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                      |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------ |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [list-shares-output.json](samba/list-shares-output.json "open original schema") |

## list-shares output Type

`object` ([list-shares output](list-shares-output.md))

## list-shares output Examples

```json
{
  "shares": [
    {
      "name": "myshare001",
      "enable_audit": false,
      "log_failed_events": false,
      "enable_recycle": false,
      "recycle_retention": 30,
      "recycle_versions": true,
      "description": "First share",
      "acls": [
        {
          "subject": "BUILTIN\\Administrators",
          "rights": "full"
        },
        {
          "subject": "Domain Controllers",
          "rights": "special"
        },
        {
          "subject": "g1",
          "rights": "rw"
        },
        {
          "subject": "Everyone",
          "rights": "ro"
        }
      ]
    },
    {
      "name": "myshare002",
      "enable_audit": true,
      "log_failed_events": false,
      "enable_recycle": true,
      "recycle_retention": 7,
      "recycle_versions": false,
      "description": "Second share",
      "acls": [
        {
          "subject": "BUILTIN\\Administrators",
          "rights": "full"
        },
        {
          "subject": "Domain Controllers",
          "rights": "special"
        },
        {
          "subject": "Everyone",
          "rights": "rw"
        }
      ]
    }
  ]
}
```

# list-shares output Properties

| Property          | Type    | Required | Nullable       | Defined by                                                                                                                                    |
| :---------------- | :------ | :------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| [shares](#shares) | `array` | Required | cannot be null | [list-shares output](list-shares-output-properties-shares.md "http://schema.nethserver.org/samba/list-shares-output.json#/properties/shares") |

## shares



`shares`

* is required

* Type: `object[]` ([Details](list-shares-output-defs-share.md))

* cannot be null

* defined in: [list-shares output](list-shares-output-properties-shares.md "http://schema.nethserver.org/samba/list-shares-output.json#/properties/shares")

### shares Type

`object[]` ([Details](list-shares-output-defs-share.md))

# list-shares output Definitions

## Definitions group share

Reference this group by using

```json
{"$ref":"http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share"}
```

| Property                                  | Type      | Required | Nullable       | Defined by                                                                                                                                                                                 |
| :---------------------------------------- | :-------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                             | `string`  | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-share-name.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/name")                     |
| [description](#description)               | `string`  | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-share-description.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/description")       |
| [browseable](#browseable)                 | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-browseable.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/browseable")               |
| [enable\_recycle](#enable_recycle)        | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-enable_recycle.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_recycle")       |
| [recycle\_versions](#recycle_versions)    | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-recycle_versions.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_versions")   |
| [recycle\_retention](#recycle_retention)  | `integer` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-recycle_retention.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_retention") |
| [enable\_audit](#enable_audit)            | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-enable_audit.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_audit")           |
| [log\_failed\_events](#log_failed_events) | `boolean` | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-log_failed_events.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/log_failed_events") |
| [acls](#acls)                             | `array`   | Optional | cannot be null | [list-shares output](list-shares-output-defs-share-properties-acls.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/acls")                           |

### name

Name of the share corresponding to the underlying directory name

`name`

* is optional

* Type: `string` ([Share name](list-shares-output-defs-share-properties-share-name.md))

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-share-name.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/name")

#### name Type

`string` ([Share name](list-shares-output-defs-share-properties-share-name.md))

### description

Free text, known also as "comment"

`description`

* is optional

* Type: `string` ([Share description](list-shares-output-defs-share-properties-share-description.md))

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-share-description.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/description")

#### description Type

`string` ([Share description](list-shares-output-defs-share-properties-share-description.md))

### browseable

If true the share is browseable to users, and is listed as a server resource. If false users must know its name to connect with it because it is not included in the network share list.

`browseable`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-browseable.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/browseable")

#### browseable Type

`boolean`

### enable\_recycle

Enable the Recycle Bin for this network share.

`enable_recycle`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-enable_recycle.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_recycle")

#### enable\_recycle Type

`boolean`

### recycle\_versions

Keeps multiple versions of deleted files with the same name. If false, only the latest version is retained.

`recycle_versions`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-recycle_versions.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_versions")

#### recycle\_versions Type

`boolean`

#### recycle\_versions Default Value

The default value is:

```json
false
```

### recycle\_retention

Number of days deleted files are retained in the Recycle Bin before permanent removal. 0 = Infinite

`recycle_retention`

* is optional

* Type: `integer`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-recycle_retention.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/recycle_retention")

#### recycle\_retention Type

`integer`

#### recycle\_retention Constraints

**minimum**: the value of this number must greater than or equal to: `0`

### enable\_audit

The basic audit log for the share is enabled

`enable_audit`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-enable_audit.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/enable_audit")

#### enable\_audit Type

`boolean`

### log\_failed\_events

Failed events are written to the audit log

`log_failed_events`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-log_failed_events.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/log_failed_events")

#### log\_failed\_events Type

`boolean`

### acls



`acls`

* is optional

* Type: `object[]` ([ACL item](list-shares-output-defs-acl-item.md))

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-share-properties-acls.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/share/properties/acls")

#### acls Type

`object[]` ([ACL item](list-shares-output-defs-acl-item.md))

## Definitions group acl\_item

Reference this group by using

```json
{"$ref":"http://schema.nethserver.org/samba/list-shares-output.json#/$defs/acl_item"}
```

| Property            | Type          | Required | Nullable       | Defined by                                                                                                                                                                   |
| :------------------ | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [subject](#subject) | `string`      | Required | cannot be null | [list-shares output](list-shares-output-defs-acl-item-properties-subject.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/acl_item/properties/subject") |
| [rights](#rights)   | Not specified | Required | cannot be null | [list-shares output](list-shares-output-defs-acl-item-properties-rights.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/acl_item/properties/rights")   |

### subject



`subject`

* is required

* Type: `string`

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-acl-item-properties-subject.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/acl_item/properties/subject")

#### subject Type

`string`

### rights



`rights`

* is required

* Type: unknown

* cannot be null

* defined in: [list-shares output](list-shares-output-defs-acl-item-properties-rights.md "http://schema.nethserver.org/samba/list-shares-output.json#/$defs/acl_item/properties/rights")

#### rights Type

unknown

#### rights Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"full"`    |             |
| `"ro"`      |             |
| `"rw"`      |             |
| `"special"` |             |
