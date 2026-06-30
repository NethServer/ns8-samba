# export-users output Schema

```txt
http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                       |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [validate-output.json](export-users/validate-output.json "open original schema") |

## export-users output Type

`object` ([export-users output](validate-output-1.md))

## export-users output Examples

```json
[
  {
    "status": "success",
    "message": "export_users",
    "records": [
      {
        "user": "alice",
        "display_name": "Alice Jordan",
        "locked": false,
        "groups": [
          "developers"
        ],
        "mail": "alice@nethserver.org",
        "must_change_password": true,
        "no_password_expiration": false
      },
      {
        "user": "bob",
        "display_name": "Robert Smith",
        "locked": false,
        "groups": [
          "support"
        ],
        "mail": "robert@nethserver.org",
        "must_change_password": true,
        "no_password_expiration": false
      }
    ]
  }
]
```

# export-users output Properties

| Property            | Type          | Required | Nullable       | Defined by                                                                                                                                                                         |
| :------------------ | :------------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [status](#status)   | Not specified | Required | cannot be null | [export-users output](validate-output-1-properties-status.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/properties/status")   |
| [message](#message) | `string`      | Required | cannot be null | [export-users output](validate-output-1-properties-message.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/properties/message") |
| [records](#records) | `array`       | Optional | cannot be null | [export-users output](validate-output-1-properties-records.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/properties/records") |

## status



`status`

* is required

* Type: unknown

* cannot be null

* defined in: [export-users output](validate-output-1-properties-status.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/properties/status")

### status Type

unknown

### status Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value       | Explanation |
| :---------- | :---------- |
| `"success"` |             |
| `"failure"` |             |

## message



`message`

* is required

* Type: `string`

* cannot be null

* defined in: [export-users output](validate-output-1-properties-message.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/properties/message")

### message Type

`string`

## records



`records`

* is optional

* Type: `object[]` ([Details](validate-output-1-defs-record-object.md))

* cannot be null

* defined in: [export-users output](validate-output-1-properties-records.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/properties/records")

### records Type

`object[]` ([Details](validate-output-1-defs-record-object.md))

# export-users output Definitions

## Definitions group record-object

Reference this group by using

```json
{"$ref":"http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object"}
```

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                              |
| :-------------------------------------------------- | :-------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [user](#user)                                       | `string`  | Required | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-user.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/user")                                     |
| [display\_name](#display_name)                      | `string`  | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-display_name.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/display_name")                     |
| [locked](#locked)                                   | `boolean` | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-locked.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/locked")                                 |
| [groups](#groups)                                   | `array`   | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-groups.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/groups")                                 |
| [mail](#mail)                                       | `string`  | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-email-address.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/mail")                            |
| [must\_change\_password](#must_change_password)     | `boolean` | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-must_change_password.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/must_change_password")     |
| [no\_password\_expiration](#no_password_expiration) | `boolean` | Optional | cannot be null | [export-users output](validate-output-1-defs-record-object-properties-no_password_expiration.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/no_password_expiration") |

### user



`user`

* is required

* Type: `string`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-user.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/user")

#### user Type

`string`

### display\_name



`display_name`

* is optional

* Type: `string`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-display_name.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/display_name")

#### display\_name Type

`string`

### locked

If true, the account is locked, preventing logins

`locked`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-locked.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/locked")

#### locked Type

`boolean`

#### locked Default Value

The default value is:

```json
false
```

### groups

List of groups

`groups`

* is optional

* Type: `string[]`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-groups.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/groups")

#### groups Type

`string[]`

### mail



`mail`

* is optional

* Type: `string` ([Email address](validate-output-1-defs-record-object-properties-email-address.md))

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-email-address.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/mail")

#### mail Type

`string` ([Email address](validate-output-1-defs-record-object-properties-email-address.md))

### must\_change\_password

If true, the user must change their password at next login

`must_change_password`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-must_change_password.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/must_change_password")

#### must\_change\_password Type

`boolean`

### no\_password\_expiration

If true, the user's password will not expire

`no_password_expiration`

* is optional

* Type: `boolean`

* cannot be null

* defined in: [export-users output](validate-output-1-defs-record-object-properties-no_password_expiration.md "http://schema.nethserver.org/ns8-samba/api-moduled/handlers/export-users/validate-output.json#/$defs/record-object/properties/no_password_expiration")

#### no\_password\_expiration Type

`boolean`
