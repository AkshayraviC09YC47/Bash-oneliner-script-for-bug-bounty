package com.example.rootcheckerjava;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.view.Gravity;
import android.graphics.Color;
import android.util.TypedValue;
import android.widget.Toast;
import java.io.File;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Arrays;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (isDeviceRooted()) {
            showToastAndExit("Rooted device detected, exiting.");
        } else {
            showSecureDeviceScreen();
        }
    }

    private boolean isDeviceRooted() {
        return checkRootFiles() || checkRootCommands() || checkMagiskZygisk();
    }

    private boolean checkRootFiles() {
        List<String> rootPaths = Arrays.asList(
                "/system/bin/su", "/system/xbin/su", "/sbin/su",
                "/system/app/Superuser.apk", "/system/xbin/mu",
                "/data/local/tmp/frida", "/data/local/tmp/frida-server"
        );
        for (String path : rootPaths) {
            if (new File(path).exists()) {
                return true;
            }
        }
        return false;
    }

    private boolean checkRootCommands() {
        return executeCommand("which su") || executeCommand("which magisk") || executeCommand("which busybox");
    }

    private boolean checkMagiskZygisk() {
        return executeCommand("getprop | grep magisk") || executeCommand("getprop | grep zygisk");
    }

    private boolean executeCommand(String command) {
        try {
            Process process = Runtime.getRuntime().exec(new String[]{"/system/bin/sh", "-c", command});
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            return reader.readLine() != null;
        } catch (Exception ignored) {
            return false;
        }
    }

    private void showToastAndExit(String message) {
        Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
        finish();
    }

    private void showSecureDeviceScreen() {
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setGravity(Gravity.CENTER);

        TextView title = new TextView(this);
        title.setText("Secure Device");
        title.setTextSize(TypedValue.COMPLEX_UNIT_SP, 28);
        title.setTextColor(Color.BLACK);
        title.setGravity(Gravity.CENTER);
        layout.addView(title);

        TextView message = new TextView(this);
        message.setText("App Created by Akshay R");
        message.setTextSize(TypedValue.COMPLEX_UNIT_SP, 18);
        message.setTextColor(Color.GRAY);
        message.setGravity(Gravity.CENTER);
        layout.addView(message);

        setContentView(layout);
    }
}
