{
  "name": "SophosIntelix_Submit_Static",
  "version": "0.1",
  "author": "SOL",
  "url": "https://github.com/TheHive-Project/Cortex-Analyzers",
  "license": "AGPL-V3",
  "description": "Submits a file to Sophos Intelix for Static Analysis",
  "dataTypeList": ["file"],
  "command": "SophosIntelix/intelix_analyzer.py",
  "baseConfig": "SophosIntelix",
  "config": {
    "service": "submit_static"
  },
  "configurationItems": [
    {
      "name": "clientID",
      "description": "Client ID for Sophos Labs Intelix",
      "type": "string",
      "multi": false,
      "required": true
    },
    {
      "name": "clientSecret",
      "description": "Client Secret for Sophos Labs Intelix",
      "type": "string",
      "multi": false,
      "required": true
    },
    {
      "name": "polling_interval",
      "description": "Define time interval between two requests attempts for the report",
      "type": "number",
      "multi": false,
      "required": false,
      "defaultValue": 60
    }
  ]
}
