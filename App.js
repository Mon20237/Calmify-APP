import React from "react";
import { FaSmile, FaFrown, FaMeh, FaRegMeh, FaSadTear } from "react-icons/fa";

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-100 to-purple-200 p-4 space-y-6">
      {/* Header */}
      <div className="bg-white shadow-md rounded-xl text-center py-6">
        <h1 className="text-3xl font-bold text-indigo-700">Calmify+</h1>
        <p className="text-gray-600 mt-2">Encuentra tu calma en un solo clic</p>
        <button className="mt-4 bg-indigo-600 text-white px-4 py-2 rounded-full">Comenzar</button>
      </div>

      {/* Cuestionario Diario */}
      <div className="bg-white p-5 rounded-xl shadow space-y-3">
        <h2 className="font-semibold text-lg">¿Cómo te sientes hoy?</h2>
        <div className="flex justify-around my-3 text-2xl text-yellow-500">
          <FaSmile /> <FaMeh /> <FaRegMeh /> <FaFrown /> <FaSadTear />
        </div>
        <div className="space-y-2 text-gray-700">
          <label className="block"><input type="radio" name="estado" /> Me siento estresado/a</label>
          <label className="block"><input type="radio" name="estado" /> Me cuesta dormir</label>
          <label className="block"><input type="radio" name="estado" /> Me siento ansioso/a sin razón</label>
          <label className="block"><input type="radio" name="estado" /> Tengo dificultad para concentrarme</label>
        </div>
        <button className="mt-3 bg-indigo-600 text-white px-4 py-2 rounded">Ver resultados</button>
      </div>

      {/* Caja de calma */}
      <div className="bg-white p-5 rounded-xl shadow space-y-3">
        <h2 className="font-semibold text-lg">Tu caja de calma</h2>
        <div className="grid grid-cols-2 gap-4">
          <button className="bg-indigo-100 px-4 py-2 rounded">Respiración guiada</button>
          <button className="bg-purple-100 px-4 py-2 rounded">Meditación</button>
          <button className="bg-blue-100 px-4 py-2 rounded">Diario emocional</button>
          <button className="bg-pink-100 px-4 py-2 rounded">Ver más</button>
        </div>
      </div>
    </div>
  );
}

export default App;