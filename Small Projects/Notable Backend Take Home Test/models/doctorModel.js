const mongoose= require('mongoose');

const Schema=mongoose.Schema;

const doctorSchema= new Schema({
    id:{type:Number, required:true, unique: true},
    first_name:{type:String, required:true},
    last_name:{type:String, required:true}
});

const Doctor=mongoose.model('Doctor',doctorSchema);

module.exports=Doctor;
