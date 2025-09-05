# set-nbalias input Schema

```txt
http://schema.nethserver.org/samba/configure-module-input.json
```

Change the basic configuration of the server

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                              |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [configure-module-input.json](samba/configure-module-input.json "open original schema") |

## set-nbalias input Type

`object` ([set-nbalias input](configure-module-input.md))

any of

* [Untitled undefined type in set-nbalias input](configure-module-input-anyof-0.md "check type definition")

* [Untitled undefined type in set-nbalias input](configure-module-input-anyof-1.md "check type definition")

## set-nbalias input Examples

```json
{
  "nbalias": "ns7fs",
  "ipaddress": "192.168.1.1",
  "adminuser": "administrator@ad.domain.org",
  "adminpass": "s3cr3t"
}
```

# set-nbalias input Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                 |
| :---------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ipaddress](#ipaddress) | `string` | Optional | cannot be null | [set-nbalias input](configure-module-input-properties-ipaddress.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/ipaddress") |
| [adminuser](#adminuser) | `string` | Optional | cannot be null | [set-nbalias input](configure-module-input-properties-adminuser.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/adminuser") |
| [adminpass](#adminpass) | `string` | Optional | cannot be null | [set-nbalias input](configure-module-input-properties-adminpass.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/adminpass") |
| [nbalias](#nbalias)     | `string` | Optional | cannot be null | [set-nbalias input](configure-module-input-properties-nbalias.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/nbalias")     |

## ipaddress



`ipaddress`

* is optional

* Type: `string`

* cannot be null

* defined in: [set-nbalias input](configure-module-input-properties-ipaddress.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/ipaddress")

### ipaddress Type

`string`

### ipaddress Constraints

**IPv4**: the string must be an IPv4 address (dotted quad), according to [RFC 2673, section 3.2](https://tools.ietf.org/html/rfc2673 "check the specification")

## adminuser



`adminuser`

* is optional

* Type: `string`

* cannot be null

* defined in: [set-nbalias input](configure-module-input-properties-adminuser.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/adminuser")

### adminuser Type

`string`

### adminuser Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## adminpass



`adminpass`

* is optional

* Type: `string`

* cannot be null

* defined in: [set-nbalias input](configure-module-input-properties-adminpass.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/adminpass")

### adminpass Type

`string`

### adminpass Constraints

**minimum length**: the minimum number of characters for this string is: `1`

## nbalias

Server alias name to access shared folders. An empty string removes the alias.

`nbalias`

* is optional

* Type: `string`

* cannot be null

* defined in: [set-nbalias input](configure-module-input-properties-nbalias.md "http://schema.nethserver.org/samba/configure-module-input.json#/properties/nbalias")

### nbalias Type

`string`

### nbalias Constraints

**maximum length**: the maximum number of characters for this string is: `15`

**pattern**: the string must match the following regular expression:&#x20;

```regexp
^([a-zA-Z][-a-zA-Z0-9]*)?$
```

[try pattern](https://regexr.com/?expression=%5E\(%5Ba-zA-Z%5D%5B-a-zA-Z0-9%5D*\)%3F%24 "try regular expression with regexr.com")
