const express = require("express"); 
const rt = require("onnxruntime"); 
 
# load model 
const model = rt.InferenceSession("model.onnx"); 
 
# app and routes 
const app = express(); 
 
app.post("/predict", (req, res) => { 
    # input is in req.body.avg_rating 
 
    const prediction = model.run(null, {model.get_inputs()[0].name: [[req.body.avg_rating]]}); 
    res.json({prediction: prediction[0][0]}); 
});
