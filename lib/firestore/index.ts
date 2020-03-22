import {firestoreImport} from 'node-firestore-import-export';
import * as firebase from 'firebase-admin';
import * as fs from 'fs';
import * as yaml from 'js-yaml';

// https://www.npmjs.com/package/node-firestore-import-export

let credential_file = fs.readFileSync('../../.firebase_credentials.yaml', 'utf8');
let credentials = yaml.safeLoad(credential_file);

firebase.initializeApp({
    apiKey: credentials.apiKey,                             
    authDomain: "YOUR_APP.firebaseapp.com",         
    databaseURL: "https://YOUR_APP.firebaseio.com", 
    storageBucket: "YOUR_APP.appspot.com",          
    messagingSenderId: "123456789"                  
});
