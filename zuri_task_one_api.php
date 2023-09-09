<?php

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if ($_SERVER['REQUEST_URI'] === '/hello') {
        $response = [ "slack_name" => "example_name",
                      "current_day" => "Monday",
                      "utc_time" => "2023-08-21T15:04:05Z",
                      "track" => "backend",
                      "github_file_url" => "https://github.com/username/repo/blob/main/file_name.ext",
                      "github_repo_url" => "https://github.com/username/repo",
                      "status_code" => 200
        ];
        echo json_encode($response);
    } else {
        // Return a 404 Not Found response
        http_response_code(404);
        echo json_encode(['error' => 'Not Found']);
    }
} else {
    // Return a 405 Method Not Allowed response for other HTTP methods
    http_response_code(405);
    echo json_encode(['error' => 'Method Not Allowed']);
}
