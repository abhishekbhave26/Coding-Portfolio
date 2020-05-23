const express = require('express');
const mongoose = require('mongoose');

const app = express();
app.use(express.json());

const port = 8000;

const uri = "mongodb+srv://abhishek:abhishek@cluster0-fhpij.mongodb.net/test?retryWrites=true&w=majority";
mongoose.connect(uri, { useNewUrlParser: true, useCreateIndex: true }
);
const connection = mongoose.connection;

connection.once('open', () => {
  console.log("MongoDB database connection established successfully");
})


const apptRouter = require('./routes/apptRoutes');
const doctorRouter = require('./routes/doctorRoutes');

app.use('/appt', apptRouter);
app.use('/doctor', doctorRouter);

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`);
});
