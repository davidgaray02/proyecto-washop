import { Injectable } from "@angular/core";
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Observable } from "rxjs";


@Injectable({
    providedIn: "root"
})

export class ApiServicio {
    private ApiUrl = "http://127.0.0.1:8000/api/v1/"; // URL to web api
    private httpOptions = {
        headers: new HttpHeaders({
            'Content-Type': 'application/json'
        })
    };
    constructor(private http: HttpClient) {
    }

    // Método genérico para realizar una solicitud GET
    public get<T>(endpoint: string): Observable<T> {
        return this.http.get<T>(this.ApiUrl + endpoint);
    }

    // Método genérico para realizar una solicitud POST
    public post<T>(endpoint: string, data: any): Observable<T> {
        return this.http.post<T>(this.ApiUrl + endpoint, data, this.httpOptions);
    }

    // Método genérico para realizar una solicitud PUT
    public put<T>(endpoint: string, data: any): Observable<T> {
        return this.http.put<T>(this.ApiUrl + endpoint, data, this.httpOptions);
    }

    // Método genérico para realizar una solicitud DELETE
    public delete<T>(endpoint: string): Observable<T> {
        return this.http.delete<T>(this.ApiUrl + endpoint);
    }


}