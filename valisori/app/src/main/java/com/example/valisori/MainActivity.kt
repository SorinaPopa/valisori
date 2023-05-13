package com.example.valisori

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.inputmethod.InputMethodManager
import android.widget.TextView
import android.widget.Toast
import androidx.activity.viewModels
import com.example.valisori.databinding.ActivityMainBinding
import com.google.android.material.textfield.TextInputLayout
import com.google.firebase.database.FirebaseDatabase

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private val mainViewModel: MainViewModel by viewModels()
    private lateinit var userInput: TextInputLayout
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        binding.lifecycleOwner = this
        binding.mainViewModel = mainViewModel
        setContentView(binding.root)
        userInput = binding.userInputText




//        sharedPreferences = getSharedPreferences(
//            getString(R.string.shared_preference_organiser), Context.MODE_PRIVATE
//        )
//        subscribeToObserver()
        openKeyboardObserver()
    }

    private fun openKeyboardObserver() {
        //initialise Firebase database and reference
        val database = FirebaseDatabase.getInstance()
        val timestamp = System.currentTimeMillis().toString()
        val myRef = database.getReference("data").child(timestamp)
        mainViewModel.onInputButtonClicked.observe(this) { value ->
            if (value) {
//                val imm = getSystemService(Context.INPUT_METHOD_SERVICE) as InputMethodManager
//                imm.showSoftInput(userInput, InputMethodManager.SHOW_IMPLICIT)
//                finish()


                myRef.setValue("Send!")
                Toast.makeText(this, "Data pushed to server with timestamp $timestamp", Toast.LENGTH_LONG).show()

            }
        }
    }

}