package com.example.valisori

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.MutableLiveData

class MainViewModel(application:Application) : AndroidViewModel(application) {
    val inputText = MutableLiveData("")
    val onInputButtonClicked = MutableLiveData(false)


    fun onClickInputButton() {
        onInputButtonClicked.value = true
    }
}