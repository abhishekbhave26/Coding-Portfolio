const mongoose= require('mongoose');

const Schema=mongoose.Schema;

const apptSchema= new Schema({
    id:{type:Number,required:true},
    patient_first_name:{type:String,required:true},
    patient_last_name:{type:String,required:true},
    datetime:{type:Date,required:true},
    kind:{type:String,required:true},
    doctor_id:{type:Number,required:true}
});

const Appt=mongoose.model('Appt',apptSchema);

module.exports=Appt;
