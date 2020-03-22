import {firestoreImport} from 'node-firestore-import-export';
import * as firebase from 'firebase-admin';
import * as fs from 'fs';
import * as yaml from 'js-yaml';

// https://www.npmjs.com/package/node-firestore-import-export

let credential_file = fs.readFileSync('../../.firebase_credentials.yaml', 'utf8');
let credentials = yaml.safeLoad(credential_file);

console.log(credentials);
