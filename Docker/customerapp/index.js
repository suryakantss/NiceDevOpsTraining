import express from 'express';
import mysql from 'mysql2/promise';
import 'dotenv/config';
const app = express();
app.use(express.json());
const PORT = process.env.PORT;
export const pool = mysql.createPool({
    host: process.env.HOST,
    user: process.env.USER,
    password: process.env.PASSWORD,
    database: process.env.DB,
    connectionLimit: process.env.CONLIMIT
});
app.get("/customers", async (req,res) => {
    let [rows, fields] = await pool.execute('select * from customers');
    return res.json(rows);
})

app.listen(PORT || 3000, () => {
    console.log('server is up [3000]');
});