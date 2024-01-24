package com.example.engexam;

import android.os.AsyncTask;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class HttpHandler extends AsyncTask<String, Integer, JSONObject> {
    @Override
    public JSONObject doInBackground(String ... arg){
        // arg[0] - host, arg[1] - query
        String url = arg[0] + arg[1];
        Request.Builder builder = new Request.Builder();
        Request request = builder.url(url).get().build();
        OkHttpClient client = new OkHttpClient().newBuilder().build();

        try {
            Response response = client.newCall(request).execute();
            JSONObject object = new JSONObject(response.body().string());
            return object;
        }
        catch (IOException | JSONException e) {
            throw new RuntimeException(e);
        }
    }
    @Override
    public void onPostExecute(JSONObject o){
        super.onPostExecute(o);
    }
}