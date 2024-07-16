package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"
	"os/exec"

	_ "github.com/lib/pq"
)

type pgSQL struct {
	host     string
	port     int
	user     string
	password string
	dbname   string
}

func addInDatahubAPI(flag bool) {
	if flag {
		// Создание команды для выполнения Python приложения
		cmd := exec.Command("python", "C:/Users/user/notes/addAPI.py", "my_api")
		fmt.Println(cmd)
		err := cmd.Run()
		if err != nil {
			fmt.Println("Ошибка при запуске Python приложения:", err)
			return
		}
	}
}

func executePythonScript(flag bool, data []string) {
	if flag {
		// Создание команды для выполнения Python приложения
		text := append([]string{"C:/Users/user/notes/script.py", "my_api"}, data...)

		cmd := exec.Command("python", text...)
		fmt.Println(cmd)
		err := cmd.Run()
		if err != nil {
			fmt.Println("Ошибка при запуске Python приложения:", err)
			return
		}
	}
}

func handler(w http.ResponseWriter, r *http.Request) {

	pg := pgSQL{"localhost", 5432, "postgres", "mysecretpassword", "mydatabase"}

	connStr := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
		pg.host, pg.port, pg.user, pg.password, pg.dbname)
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		log.Fatal(err)
	}

	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}

	rows, err := db.Query("SELECT name, age FROM users")
	if err != nil {
		log.Fatal(err)
	}
	defer rows.Close()

	addInDatahubAPI(false)

	executePythonScript(true, []string{"up", "users"})

	for rows.Next() {
		var name string
		var age int
		if err := rows.Scan(&name, &age); err != nil {
			log.Fatal(err)
		}
		fmt.Fprintf(w, "Name: %s, Age: %d\n", name, age)
	}

}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8888", nil))
}
