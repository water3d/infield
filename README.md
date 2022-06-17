Infield
=============
Infield is a unified API for retrieving timeseries earth observation and modeling data from cloud data
sources.

Current Support:
 * Nothing yet. Sorry. Early days!

Planned Support:
 * Earth Engine
 * NASA LPDAAC AppEEARS
 * OpenET (via [`openet_client`](https://github.com/water3d/openet-client))
 * SSEBOP (via Earth Engine and [OpenET SSEBOP Code](https://github.com/Open-ET/openet-ssebop))
 * [THREDDS Data Servers](https://github.com/Unidata/tds) (via [`siphon`](https://github.com/Unidata/siphon) or the REST API)

Planned methods:
 * A standard interface to provide a set of coordinates, a date range, and a return type (JSON, data frame, etc) and obtain the data from any of the above data sources
 * Fully custom parameter sending and data retrieval