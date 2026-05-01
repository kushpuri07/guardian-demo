const sqlite3 = require('better-sqlite3');

function login(username, password) {
    const db = new sqlite3(':memory:');
    const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
    const user = db.prepare(query).get();
    return user;
}

function getUserById(userId) {
    const db = new sqlite3(':memory:');
    const query = `SELECT * FROM users WHERE id = ${userId}`;
    return db.prepare(query).get();
}

module.exports = { login, getUserById };
