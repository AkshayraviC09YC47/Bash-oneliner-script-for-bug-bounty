package com.example.rootcheckerjava;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.widget.TextView;
import android.widget.LinearLayout;
import android.graphics.Color;
import android.view.Gravity;
import android.util.TypedValue;
import android.widget.Toast;
import java.io.File;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        if (isDeviceRooted() || checkMagisk() || checkZygisk()) {
            showToastAndExit("Rooted device detected, exiting");
        } else {
            showSecureDeviceScreen();
        }
    }

    // 🛡️ Check if device is rooted
    private boolean isDeviceRooted() {
        String[] rootPaths = {
                "/system/bin/su", "/system/xbin/su", "/sbin/su",
                "/system/sd/xbin/su", "/system/app/Superuser.apk",
                "/system/bin/.ext/.su", "/system/usr/we-need-root/su-backup",
                "/system/xbin/mu", "/data/local/tmp/su"
        };
        for (String path : rootPaths) {
            if (new File(path).exists()) {
                return true;
            }
        }
        return checkCommand("which su") || checkCommand("su -c 'id'");
    }

    // 🛡️ Check for Magisk (even if renamed)
    private boolean checkMagisk() {
        String[] magiskPaths = {
                "/sbin/.magisk", "/cache/.magisk", "/data/adb/magisk",
                "/data/adb/modules", "/data/adb/magisk.img", "/data/adb/magisk.db"
        };
        for (String path : magiskPaths) {
            if (new File(path).exists()) {
                return true;
            }
        }
        return checkCommand("getprop persist.magisk.hide") ||
               checkCommand("ls /dev | grep magisk");
    }

    // 🛡️ Check for Zygisk (even if Magisk Hide is enabled)
    private boolean checkZygisk() {
        return checkCommand("getprop | grep zygisk") ||  // System properties
               checkCommand("cat /proc/self/status | grep TracerPid") ||  // Process tracing
               checkCommand("ls /dev | grep magisk") ||  // Magisk-related devices
               checkCommand("cat /proc/self/maps | grep 'zygisk'") ||  // Memory maps
               checkCommand("ps -A | grep -E 'zygote|zygisk'");  // Detect Zygote/Zygisk
    }

    // 🔍 Execute shell commands to check root/Zygisk/Magisk traces
    private boolean checkCommand(String command) {
        try {
            Process process = Runtime.getRuntime().exec(new String[]{"sh", "-c", command});
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String output = reader.readLine();
            return output != null && !output.isEmpty();
        } catch (Exception ignored) {}
        return false;
    }

    // 🚨 Show Toast & Exit App
    private void showToastAndExit(String message) {
        new Handler(Looper.getMainLooper()).post(() -> {
            Toast.makeText(getApplicationContext(), message, Toast.LENGTH_LONG).show();
            new Handler().postDelayed(() -> {
                finishAffinity(); // Close all app activities
                System.exit(0); // Force quit
            }, 2000); // Small delay to ensure toast is shown
        });
    }

    // ✅ Display Secure Message if No Root is Found
    private void showSecureDeviceScreen() {
        LinearLayout layout = new LinearLayout(this);
        layout.setOrientation(LinearLayout.VERTICAL);
        layout.setGravity(Gravity.CENTER);
        layout.setPadding(32, 32, 32, 32);

        TextView title = new TextView(this);
        title.setText("Secure Device");
        title.setTextSize(TypedValue.COMPLEX_UNIT_SP, 28);
        title.setTextColor(Color.BLACK);
        title.setGravity(Gravity.CENTER);
        layout.addView(title);

        TextView creator = new TextView(this);
        creator.setText("App created by Akshay R");
        creator.setTextSize(TypedValue.COMPLEX_UNIT_SP, 16);
        creator.setTextColor(Color.GRAY);
        creator.setGravity(Gravity.CENTER);
        layout.addView(creator);

        setContentView(layout);
    }
}
